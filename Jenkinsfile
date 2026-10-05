pipeline {
    agent any

    // Variables globales
    environment {
        DOCKER_IMAGE = 'mariembelghouthi/counter-app:latest'
        DOCKER_CREDS = credentials('docker-hub-credentials')
    }

    stages {
        // -------------------------------------------------------------
        // ÉTAPE 1 : Build de l'environnement Python & Tests unitaires
        // -------------------------------------------------------------
        stage('1. Build & Tests Unitaires') {
            steps {
                echo 'Execution des tests unitaires Python...'
                // Installation des dépendances et exécution du test_app.py
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r app/requirements.txt
                    python3 -m unittest discover -s app -p "test_*.py"
                '''
            }
        }

        // -------------------------------------------------------------
        // ÉTAPE 2 : Build de l'image Docker & Publication sur Docker Hub
        // -------------------------------------------------------------
        stage('2. Build & Push Image Docker') {
            steps {
                echo 'Fabrication de l\'image Docker...'
                sh "docker build -t ${DOCKER_IMAGE} ."

                echo 'Connexion à Docker Hub et publication...'
                sh '''
                    echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin
                    docker push ${DOCKER_IMAGE}
                '''
            }
        }
    }

    // Nettoyage automatique après l'exécution du pipeline
    post {
        always {
            echo 'Nettoyage des images locales...'
            sh "docker rmi ${DOCKER_IMAGE} || true"
        }
    }
}