pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git(url: 'https://github.com/galkinator/WorldOfGames.git', branch: main)
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t scores-game .'
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
                sh 'docker stop scores_test'
                sh 'docker rm scores_test'
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
