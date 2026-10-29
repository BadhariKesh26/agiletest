pipeline {
    agent any
    stages {
        stage('Build & Push') {
            steps {
                sh "docker build -t badharikesh26/bill-calc:latest ."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'U', passwordVariable: 'P')]) {
                    sh "echo \$P | docker login -u \$U --password-stdin"
                    sh "docker push badharikesh26/bill-calc:latest"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "kubectl apply -f k8s.yaml"
                sh "kubectl rollout restart deployment/bill-app"
            }
        }
    }
}