pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-devops-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop ai-devops-container || true
                docker rm ai-devops-container || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name ai-devops-container -p 5000:5000 ai-devops-app'
            }
        }
    }
}