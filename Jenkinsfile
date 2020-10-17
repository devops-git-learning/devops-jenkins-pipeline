pipeline {
    agent {label 'node1'}

    stages {
        stage('unit test') {
            steps {
                sh 'docker images'
            }
        }
        stage('build docker image'){
            steps{
                withCredentials([string(credentialsId:'pdcokerhub', variable: 'mydockerhub')]) {
                sh 'docker login -u pk1dockerhub -p ${mydockerhub}'
                sh 'docker build -t my-pipeline-web:0.0.${BUILD_NUMBER} .'
                sh 'docker tag my-pipeline-web:0.0.${BUILD_NUMBER} docker.io/pk1dockerhub/ my-pipeline-web:0.0.${BUILD_NUMBER}'
                sh 'docker push docker.io/pk1dockerhub/ my-pipeline-web:0.0.${BUILD_NUMBER}'
                }
              }               
            }
        stage ('deploy image'){
            steps{
                sh 'docker run --name my-jenkins-pipeline-web -d -p 8001:8001 my-pipeline-web:0.0.${BUILD_NUMBER}'
            }
        }
        
    }
}


