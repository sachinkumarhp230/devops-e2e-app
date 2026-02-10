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
		    agent {
			    docker {
				    image 'python:3.11-slim'
				}
			}
			steps {
			    sh'''
				    python -m venv venv
					. venv/bin/activate
					pip install -r requiremans.txt
					pytest
				'''
			}
		}
		
		stage('Build image') {
			steps {
				docker build -t devops-e2e-app:${BUILD_NUMBER} .
			} 
		}
		
		stage('Publish') {
			steps {
				withCredentials([usernamePassword(
					credentialsId: 'dockerhub-creds',
					usernameVariable: 'DOCKER_USER',
					passwordVariable: 'DOCKER_PASS'
				)]) {
					sh '''
						docker tag devops-e2e-app:${BUILD_NUMBER} \
						${DOCKER_USER}/devops-e2e-app:${BUILD_NUMBER}

						echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
						docker push ${DOCKER_USER}/devops-e2e-app:${BUILD_NUMBER}
					'''
				}
			}
		}
	}
}