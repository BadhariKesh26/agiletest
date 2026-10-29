pipeline {
    agent any
    environment {
        DOCKER_USER = 'badharikesh26'
        REPO_NAME   = 'agiletest'
        PATH        = "C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"

        BUILDKIT_HTTP_TIMEOUT = '300'
    }
    stages {
        stage('Checkout Source Code') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/BadhariKesh26/agiletest.git']])
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'U', passwordVariable: 'P')]){
                        bat "docker login -u %USER% -p %PASS%"
                        dir('latest')
                           
                            bat "docker build --pull=false -t %DOCKER_USER%/%REPO_NAME%:latest."
                            bat "docker push %DOCKER_USER%/%REPO_NAME%:latest"
                        }
                    }
                }
            }
        }
    }
}
