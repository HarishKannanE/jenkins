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
                echo 'Running python hello world script...'
                sh 'python3 test_script.py'
            }
        }
        //stage('test') {
        //    steps {
        //        echo 'Running test...'
        //        sh 'echo "Running step placeholder"'
        //    }
        //}
        //stage('archive') {
        //    steps {
        //        echo 'Archiing...'
        //        archiveArtifacts artifacts: '**/*.txt', fingerprint: true
        //    }
        //}
    }
    post {
        success {
            echo 'Job completed successfully.'
        }
        failure {
            echo 'Job failed, something went wrong.'
        }
    }
}