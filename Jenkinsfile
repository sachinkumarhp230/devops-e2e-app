pipeline {
    agent any

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
                  python3 --version
                  pip3 install -r requirements.txt
                  pytest
                '''
            }
        }
    }
}
