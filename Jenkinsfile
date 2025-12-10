pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo "Build step"'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'echo "Test step"'
            }
        }
    }
}