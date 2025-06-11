pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/abhimanyu8829/selenium-grid-devopsfarm.git'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh 'docker compose up --wait --build'
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
                sh 'docker compose down --volumes --remove-orphans'
            }
        }
    }
}

