pipeline {
    agent any
    
    stages {
        stage('Install Python and pip') {
            steps {
                sh '''
                    apt-get update -y
                    apt-get install -y python3 python3-pip
                    python3 --version
                    pip3 --version
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
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Integration Test') {
            steps {
                echo ' Starting integration test...'
                script {
                    try {
                        sh 'python3 integration_test.py'
                    } catch (Exception e) {
                        error('Integration test failed!')
                    }
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                sh 'pkill -f "python3 service" || true'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo ' Pipeline failed!'
        }
    }
}