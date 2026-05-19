pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Test Application') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-devops-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop ai-devops-container || true'
                sh 'docker rm ai-devops-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name ai-devops-container -p 5000:5000 ai-devops-app'
            }
        }
    }

    post {
        failure {
            sh 'python3 analyze_real_jenkins.py'
        }
    }
}