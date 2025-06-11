pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/abhimanyu8829/selenium-grid-devopsfarm.git'
            }
        }

        stage('Build and Run Selenium Test') {
            steps {
                /usr/local/bin/docker-compose up --build --exit-code-from test-runner
            }
        }

        stage('Display Result') {
            steps {
                script {
                    def result = readFile 'test/result.log'
                    echo result
                }
            }
        }

        stage('Clean Up') {
            steps {
                sh 'docker-compose down --volumes --remove-orphans'
            }
        }
    }
}

