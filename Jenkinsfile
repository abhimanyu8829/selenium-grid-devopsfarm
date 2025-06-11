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
                sh '''
                    /usr/local/bin/docker-compose up --build --exit-code-from test-runner
                '''
            }
        }

        stage('Display Result') {
            steps {
                echo 'Test execution complete!'
            }
        }
    }
}

