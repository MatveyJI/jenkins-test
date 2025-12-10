pipeline {
    agent {
        docker {
            image 'python:3.11-alpine'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Unit Tests') {
            steps {
                echo 'Running unit tests (if any)...'
                sh 'echo "No unit tests configured"'
            }
        }
        
        stage('Integration Test') {
            steps {
                echo 'Starting integration test...'
                script {
                    try {
                        sh 'python integration_test.py'
                    } catch (Exception e) {
                        error('Integration test failed!')
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
            sh 'pkill -f "python service" || true'
        }
        success {
            echo ' All tests passed!'
        }
        failure {
            echo ' Pipeline failed!'
        }
    }
}