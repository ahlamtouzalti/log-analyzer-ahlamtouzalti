pipeline {
    agent any
    
    stages {
        stage('Start') {
            steps {
                echo 'Début de l\'analyse des logs'
            }
        }
        
        stage('Analyze') {
            steps {
                sh 'python3 log_analyzer.py'
            }
        }
        
        stage('End') {
            steps {
                echo 'Fin du pipeline'
            }
        }
    }
    
}
