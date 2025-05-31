pipeline {
    agent any
    stages {
        stage('clone repo') {
            steps {
                echo 'cloning repository...'
                checkout scm
            }
        }
        stage('build') {
            steps {
                echo 'Running build...'
                sh 'echo "Build step placeholder"'
            }
        }
        stage('test') {
            steps {
                echo 'Running test...'
                sh 'echo "Running step placeholder"'
            }
        }
        stage('archive') {
            steps {
                echo 'Archiing...'
                archiveArtifacts artifacts: '**/*.txt', fingerprint: true
            }
        }
    }
}