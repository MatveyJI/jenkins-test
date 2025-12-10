pipeline {
    agent any
    
    stages {
        stage('Check Python') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version || echo "pip3 not found, installing via get-pip.py..."
                '''
            }
        }
        
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m pip install --user flask requests
                '''
            }
        }
        
        stage('Integration Test') {
            steps {
                echo 'Starting integration test...'
                script {
                    try {
                        sh 'python3 integration_test.py'
                    } catch (Exception e) {
                        error('Integration test failed!')
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo ' Pipeline finished'
            sh 'pkill -f "python3 service" || true'
        }
        success {
            echo ' All tests passed!'
        }
        failure {
            echo ' Pipeline failed!'
        }
    }
}