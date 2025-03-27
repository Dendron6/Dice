pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Install Playwright Browsers') {
            steps {
                sh '''
                . venv/bin/activate
                playwright install
                '''
            }
        }
        
        stage('Lint') {
            steps {
                sh '''
                . venv/bin/activate
                ruff check .
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                withEnv(['PYTHONPATH=.']) {
                    withCredentials([
                        string(credentialsId: 'DICE_URL', variable: 'DICE_URL'),
                        string(credentialsId: 'DICE_USERNAME', variable: 'DICE_USERNAME'),
                        string(credentialsId: 'DICE_PASSWORD', variable: 'DICE_PASSWORD')
                    ]) {
                        sh '''
                        . venv/bin/activate
                        pytest tests/test_dice.py -v
                        '''
                    }
                }
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'test-results/**/*', allowEmptyArchive: true
            junit 'test-results/**/*.xml', allowEmptyResults: true
        }
    }
} 