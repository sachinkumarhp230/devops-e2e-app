pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/sachinkumarhp230/devops-e2e-app.git'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('Build Image') {
			steps {
				sh '''
					docker build -t devops-e2e-app:${BUILD_NUMBER} .
				'''
			}
		}
    }
}