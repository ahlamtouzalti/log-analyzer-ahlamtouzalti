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
                // Exécuter le script log_analyzer.py
                // Utiliser 'sh' pour Linux/Mac ou 'bat' pour Windows
                sh 'python3 log_analyzer.py' // Pour Linux/Mac
                // OU
                // bat 'python log_analyzer.py' // Pour Windows (décommentez cette ligne si vous êtes sur Windows)
            }
        }
        stage('End') {
            steps {
                echo 'Fin du pipeline'
            }
        }
    }
}
