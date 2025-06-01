pipeline {
    agent any

    stages {
        stage('Checkout zz') {
            steps {
                git(url: 'https://github.com/galkinator/WorldOfGames.git', branch: main)
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose up'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5000'
                sleep(time:10, unit:"SECONDS")  // Wait for Flask to start
            }
        }

        stage('Test') {
            steps {
                sh 'python3 e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker-compose down'
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
