"""
Sample realistic Resume and Job Description for 1-click interactive demo.
Matches the exact scenarios from the design specification:
- Exact/Synonym match: Java, Spring Boot, REST APIs, PostgreSQL, Docker, AWS S3
- Partial match: Kafka (JD) vs RabbitMQ (Resume)
- Missing skills: Kubernetes (Critical), Terraform (Preferred), AWS Lambda (Preferred)
- Experience: 4 years (Resume) vs 5+ years (JD)
"""

SAMPLE_RESUME_TEXT = """Alex Morgan
alex.morgan@techmail.io | +1 (555) 432-8921 | San Francisco, CA
linkedin.com/in/alexmorgan-dev | github.com/alexmorgan-tech

PROFESSIONAL SUMMARY
Dedicated Senior Software Engineer with 4 years of hands-on experience designing, developing, and deploying scalable distributed backend microservices and cloud-native applications. Proficient in Java, Spring Boot, REST APIs, and relational databases with a strong emphasis on clean code, automated testing, and performance optimization.

TECHNICAL SKILLS
• Languages: Java (8/11/17), SQL, Python, JavaScript
• Frameworks & Libraries: Spring Framework, Spring Boot, Hibernate, JUnit, Mockito, Express.js
• Databases & Storage: PostgreSQL, MySQL, Redis, Amazon S3
• Cloud & DevOps: Amazon Web Services (AWS S3, EC2), Docker, Git, CI/CD pipelines, Maven, Linux
• Messaging & Protocols: RabbitMQ, REST APIs, HTTP/HTTPS, WebSockets
• Methodologies: Agile / Scrum, Test-Driven Development (TDD), Microservices Architecture

PROFESSIONAL EXPERIENCE

Senior Backend Engineer | FinTech Innovations Inc.
San Francisco, CA | Jan 2022 – Present
• Engineered high-throughput financial transaction processing services in Java and Spring Boot, managing over 500,000 daily active requests.
• Designed cloud-based object storage solutions using Amazon S3 for secure, encrypted customer statements and financial audit reports.
• Implemented asynchronous event-driven architectures utilizing RabbitMQ message queues to decouple order settlement from notification services.
• Optimized PostgreSQL database queries and connection pooling, reducing p99 latency by 35% across core reporting endpoints.
• Containerized microservices using Docker and collaborated with DevOps engineers to streamline CI/CD deployment pipelines.

Software Engineer | CloudScale Solutions
Austin, TX | Jun 2020 – Dec 2021
• Developed REST APIs using Spring Boot and Java to power enterprise resource planning portals.
• Integrated Redis caching layers to speed up user session lookups and reduce primary database load.
• Collaborated in an Agile Scrum team of 8 engineers, participating in bi-weekly sprint planning, code reviews, and architectural spikes.
• Authored comprehensive automated test suites using JUnit and Mockito, maintaining over 85% branch coverage.

KEY PROJECTS

Enterprise Cloud Storage & Archive Manager | Java, Spring Boot, Amazon S3, React
• Built a secure document management microservice providing multi-tenant access control and automated lifecycle archiving to Amazon S3 storage classes.
• Created RESTful endpoints with Spring Security JWT authentication and role-based access management.

Event-Driven Order Processing Engine | Java, RabbitMQ, PostgreSQL, Docker
• Implemented an order routing simulator testing high-volume message consumption and idempotency handling across distributed worker nodes.

EDUCATION
Bachelor of Science in Computer Science
University of California, Berkeley | 2016 – 2020
• Relevant Coursework: Data Structures & Algorithms, Distributed Systems, Database Management, Operating Systems

CERTIFICATIONS
• AWS Certified Cloud Practitioner (Amazon Web Services, 2023)
"""

SAMPLE_JD_TEXT = """Job Title: Senior Backend Software Engineer - Cloud Platform
Company: Apex Cloud Technologies
Location: San Francisco, CA (Hybrid / Remote)

About the Role:
Apex Cloud Technologies is seeking an experienced Senior Backend Software Engineer to join our Core Platform Team. In this role, you will be responsible for building high-scale, resilient microservices that power our real-time cloud data infrastructure.

Responsibilities:
• Design, architect, and deliver robust, secure, and highly available distributed microservices.
• Develop performant REST APIs and event-driven data streaming pipelines.
• Collaborate with cross-functional engineering teams, product managers, and site reliability engineers.
• Write clean, maintainable, and thoroughly tested code with high unit and integration test coverage.
• Participate in architectural design reviews, technical mentorship, and Agile sprint ceremonies.

Requirements (Must Have):
• 5+ years of professional software engineering experience building backend systems.
• Strong proficiency in Java and modern enterprise frameworks (Spring Boot).
• Extensive experience developing and consuming REST APIs in production environments.
• Solid background in relational databases (PostgreSQL or MySQL) including query tuning and indexing.
• Hands-on experience with containerization technologies (Docker) and cloud storage (AWS S3).
• Direct experience with distributed message streaming systems (Apache Kafka).
• Experience deploying and orchestrating microservices in container clusters using Kubernetes (K8s).
• Bachelor’s degree in Computer Science, Software Engineering, or equivalent practical experience.

Preferred Qualifications (Nice to Have):
• Infrastructure as Code (IaC) experience using Terraform.
• Experience with serverless architectures using AWS Lambda.
• Familiarity with metrics, monitoring, and observability tools such as Prometheus and Grafana.
• AWS Certified Solutions Architect or Developer Associate certification.
• Excellent communication, problem-solving, and cross-team collaboration skills.
"""
