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
                    /usr/local/bin/docker-compose down || true
                    /usr/local/bin/docker-compose up --build --exit-code-from test-runner
                '''
            }
        }

        stage('Display Result') {
            steps {
                echo 'Test execution complete!'
                sh 'cat result.txt || echo "❌ result.txt not found!"'
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'result.txt', fingerprint: true
            }
        }
    }
}

