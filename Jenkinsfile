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
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install --upgrade pip setuptools wheel
                pip install --prefer-binary -r requirements.txt
                '''
            }
        }
        
        stage('Install Playwright Browsers') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                playwright install
                '''
            }
        }
        
        stage('Lint') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                ruff check .
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                withEnv(['PYTHONPATH=.', 'CI=true']) {
                    withCredentials([
                        string(credentialsId: 'DICE_URL', variable: 'DICE_URL'),
                        string(credentialsId: 'DICE_USERNAME', variable: 'DICE_USERNAME'),
                        string(credentialsId: 'DICE_PASSWORD', variable: 'DICE_PASSWORD')
                    ]) {
                        bat '''
                        call venv\\Scripts\\activate.bat
                        mkdir test-results
                        pytest tests/test_dice.py -v --junitxml=test-results/results.xml
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