pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }
    }
}
