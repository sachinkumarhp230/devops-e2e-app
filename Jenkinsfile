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
		
		stage('Update GitOps Repo (DEV)') {
			steps {
				withCredentials([usernamePassword(
					credentialsId: 'github-creds',
					usernameVariable: 'GIT_USER',
					passwordVariable: 'GIT_PASS'
				)]) {
					sh '''
						rm -rf gitops
						git clone https://${GIT_USER}:${GIT_PASS}@github.com/sachinkumarhp230/devops-e2e-gitops.git gitops

						cd gitops/dev

						sed -i "s|image: .*|image: ${GIT_USER}/devops-e2e-app:${BUILD_NUMBER}|" app.yaml

						git config user.email "ci@jenkins"
						git config user.name "jenkins-ci"

						git add app.yaml
						git commit -m "Update image to ${BUILD_NUMBER} (DEV)"
						git push origin main
					'''
				}
			}
		}

	}
}