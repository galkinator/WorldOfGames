pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t blabla .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5001 blabla'
                sleep(time:10, unit:"SECONDS")  // Wait for Flask to start
            }
        }

        stage('Test') {
            steps {
                sh 'python3 tests/e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop blabla'
                sh 'docker rm blabla'
            }
        }
    }

    post {
        failure {
            echo "❌ Build or tests failed."
        }
        success {
            echo "✅ Application built and tested successfully."
        }
    }
}
