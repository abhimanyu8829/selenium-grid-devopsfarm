pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/abhimanyu8829/selenium-grid-devopsfarm.git'
            }
        }

        stage('Clean Old Containers') {
            steps {
                sh '''
                    echo "🧹 Cleaning up old containers if any..."
                    docker ps -a --filter "name=selenium-hub" --format "{{.ID}}" | xargs -r docker rm -f || true
                    docker ps -a --filter "name=selenium-grid-devopsfarm-chrome" --format "{{.ID}}" | xargs -r docker rm -f || true
                    docker ps -a --filter "name=selenium-grid-devopsfarm-firefox" --format "{{.ID}}" | xargs -r docker rm -f || true
                    docker ps -a --filter "name=test-runner" --format "{{.ID}}" | xargs -r docker rm -f || true
                '''
            }
        }

        stage('Build and Run Selenium Test') {
            steps {
                sh '''
                    echo "📦 Running docker-compose build and test..."
                    /usr/local/bin/docker-compose down || true
                    /usr/local/bin/docker-compose up --build --exit-code-from test-runner
                '''
            }
        }

        stage('Display Result') {
            steps {
                echo '✅ Test execution complete!'
            }
        }
    }
}

