pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo ' Cloning repository...'
                checkout scm
            }
        }
        
        stage('Integration Test') {
            steps {
                echo ' Starting integration test...'
                sh '''
                    chmod +x integration_test.sh
                    ./integration_test.sh
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo ' All tests passed!'
        }
        failure {
            echo ' Pipeline failed!'
        }
    }
}