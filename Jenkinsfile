pipeline {
    agent any
    
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
        
        stage('Cleanup') {
            steps {
                echo 'Cleaning up after tests...'
                sh 'pkill -f "python service" || true'
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