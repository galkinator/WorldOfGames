pipeline {
    agent any

    stages {
        stage('checkout'){
            steps{
                git(url: 'https://github.com/galkinator/WorldOfGames.git', branch: 'main')
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d --remove-orphans'
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
                sh 'docker-compose down'
                sh 'docker-compose push'
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
