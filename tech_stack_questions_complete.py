"""
Tech Stack Question Generator - Generates relevant technical questions
"""

import random


class TechStackQuestionGenerator:
    """Generates technical questions tailored to candidate's declared tech stack"""

    def __init__(self):
        self.question_bank = {
            "python": [
                "What is the difference between lists and tuples in Python?",
                "Explain decorators in Python and provide a use case.",
                "How does Python's garbage collection work?",
                "What are list comprehensions and how do they improve code readability?",
                "Explain the difference between 'is' and '==' in Python."
            ],
            "javascript": [
                "Explain the concept of closures in JavaScript with an example.",
                "What is the difference between 'let', 'const', and 'var'?",
                "How does event delegation work in JavaScript?",
                "Explain promises and async/await in JavaScript.",
                "What is the event loop in JavaScript and how does it work?"
            ],
            "java": [
                "What is the difference between an interface and an abstract class in Java?",
                "Explain the concept of multithreading in Java.",
                "What are Java Collections and which ones do you use most frequently?",
                "How does garbage collection work in Java?",
                "Explain the SOLID principles in Java development."
            ],
            "react": [
                "Explain the Virtual DOM and how React uses it for performance optimization.",
                "What are React Hooks and why were they introduced?",
                "How do you manage state in a React application?",
                "What is the difference between controlled and uncontrolled components?",
                "Explain the component lifecycle methods in React."
            ],
            "angular": [
                "What are Angular directives and what types exist?",
                "Explain dependency injection in Angular.",
                "What is the difference between Observables and Promises in Angular?",
                "How does change detection work in Angular?",
                "What are Angular modules and why are they important?"
            ],
            "vue": [
                "Explain the Vue component lifecycle hooks.",
                "What is the difference between computed properties and watchers in Vue?",
                "How does Vue's reactivity system work?",
                "What are slots in Vue and when would you use them?",
                "Explain Vuex and how it helps with state management."
            ],
            "django": [
                "Explain Django's MVT (Model-View-Template) architecture.",
                "What are Django middleware and how do they work?",
                "How does Django's ORM handle database queries?",
                "Explain Django signals and provide a use case.",
                "How do you handle authentication and authorization in Django?"
            ],
            "flask": [
                "What makes Flask a 'micro' framework?",
                "How do you handle routing in Flask?",
                "Explain Flask blueprints and when you would use them.",
                "How do you manage database connections in Flask?",
                "What is the difference between Flask and Django?"
            ],
            "express": [
                "How does middleware work in Express.js?",
                "Explain the request-response cycle in Express.",
                "How do you handle errors in Express applications?",
                "What are route parameters and query strings in Express?",
                "How do you implement authentication in Express.js?"
            ],
            "sql": [
                "Explain the difference between INNER JOIN, LEFT JOIN, and RIGHT JOIN.",
                "What are indexes and how do they improve database performance?",
                "Explain database normalization and why it is important.",
                "What is the difference between DELETE, TRUNCATE, and DROP?",
                "How do you optimize a slow SQL query?"
            ],
            "postgresql": [
                "What makes PostgreSQL different from other relational databases?",
                "Explain JSONB data type in PostgreSQL and its advantages.",
                "What are PostgreSQL extensions and name a few useful ones?",
                "How does PostgreSQL handle concurrency?",
                "Explain full-text search capabilities in PostgreSQL."
            ],
            "mysql": [
                "What storage engines does MySQL support and what are their differences?",
                "Explain transactions and ACID properties in MySQL.",
                "How do you handle replication in MySQL?",
                "What are stored procedures and when would you use them?",
                "Explain the difference between CHAR and VARCHAR in MySQL."
            ],
            "mongodb": [
                "Explain the document model in MongoDB.",
                "What is the difference between SQL and NoSQL databases?",
                "How do you design schemas in MongoDB?",
                "Explain indexing strategies in MongoDB.",
                "What are aggregation pipelines in MongoDB?"
            ],
            "redis": [
                "What data structures does Redis support?",
                "How do you use Redis for caching?",
                "Explain Redis persistence mechanisms.",
                "What is the difference between Redis and Memcached?",
                "How can Redis be used for pub/sub messaging?"
            ],
            "docker": [
                "What is the difference between a Docker image and a container?",
                "Explain Docker volumes and why they are important.",
                "How do you optimize Docker images for size and performance?",
                "What is the purpose of Docker Compose?",
                "Explain the Docker networking model."
            ],
            "kubernetes": [
                "What are Pods in Kubernetes?",
                "Explain the difference between Deployments and StatefulSets.",
                "How does Kubernetes handle load balancing?",
                "What are Kubernetes Services and why are they needed?",
                "Explain horizontal pod autoscaling in Kubernetes."
            ],
            "aws": [
                "Explain the difference between EC2 and Lambda.",
                "What is the purpose of S3 and what are its use cases?",
                "How does AWS handle security and access control?",
                "Explain VPC and its components in AWS.",
                "What is the difference between RDS and DynamoDB?"
            ],
            "git": [
                "Explain the difference between merge and rebase in Git.",
                "What is the purpose of branches in Git?",
                "How do you resolve merge conflicts?",
                "Explain Git workflow strategies (GitFlow, GitHub Flow, etc.).",
                "What is the difference between 'git pull' and 'git fetch'?"
            ],
        }

        self.generic_questions = [
            "Describe a challenging technical problem you have solved recently. What was your approach?",
            "How do you stay updated with new technologies and best practices in your field?",
            "Explain a project you are proud of. What technologies did you use and why?",
            "How do you approach debugging when you encounter a difficult issue?",
            "What factors do you consider when choosing between different technologies for a project?"
        ]

    def normalize_tech_name(self, tech):
        """Normalize technology names to match question bank keys"""
        tech_lower = tech.lower().strip()

        variations = {
            "js": "javascript",
            "node": "express",
            "nodejs": "express",
            "node.js": "express",
            "reactjs": "react",
            "react.js": "react",
            "angularjs": "angular",
            "vue.js": "vue",
            "vuejs": "vue",
            "postgres": "postgresql",
            "mongo": "mongodb",
            "k8s": "kubernetes",
            "py": "python",
        }

        return variations.get(tech_lower, tech_lower)

    def generate_questions(self, tech_stack, num_questions=5):
        """
        Generate technical questions based on candidate's tech stack

        Args:
            tech_stack: List of technologies the candidate knows
            num_questions: Number of questions to generate (default 5)

        Returns:
            List of technical question strings
        """
        questions = []
        normalized_stack = [self.normalize_tech_name(tech) for tech in tech_stack]

        # Try to get questions for each technology in the stack
        for tech in normalized_stack:
            if tech in self.question_bank:
                available_questions = self.question_bank[tech]
                if available_questions:
                    question = random.choice(available_questions)
                    if question not in questions:
                        questions.append(question)

        # If we don't have enough tech-specific questions, add generic ones
        while len(questions) < num_questions:
            generic_q = random.choice(self.generic_questions)
            if generic_q not in questions:
                questions.append(generic_q)

        # Limit to requested number of questions
        return questions[:num_questions]
