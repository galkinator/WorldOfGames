pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh 'git clone https://github.com/galkinator/WorldOfGames.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t scores-game .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5000 -v $PWD/dummy/Scores.txt:/Scores.txt --name scores_test scores-game'
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
