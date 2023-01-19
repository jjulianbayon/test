DOCKER_REGISTRY = 'jjulianbayon'
BUILDER_NAME = 'mbuilder'
SERVICE = 'testArq'
TAG = 'v0.1'

pipeline {

   agent any

    stages {
        stage('Init') {
            agent any
         steps {
      	    withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
            	    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                   }  
               }
        }       

        stage('Build') {
            steps {
                echo 'Create building image..'
                //sh 'docker build -t jjulianbayon/test:latest .'
             sh """
                docker buildx create --name $BUILDER_NAME
                docker buildx use $BUILDER_NAME
                docker buildx inspect --bootstrap
                ## Check step
                docker buildx ls
            """

                //sh 'docker buildx build -t jjulianbayon/test:latest .'
            }
        }
        stage ('Build multi-arch image'){
            step {
                sh """
                    docker buildx build --platform linux/amd64,linux/arm64 --push -t $DOCKER_REGISTRY/$SERVICE:$TAG .
                """    
            }
        }
        //stage('Test') {
        //    steps {
        //        echo 'Testing..'
        //        sh 'docker run --rm -e CI=true jjulianbayon/test pytest'
        //    }
        //}
        //stage('Publish') {
        //    steps {
        //    echo 'Publishing image to DockerHub..'         
        //     sh 'docker push jjulianbayon/test:latest'
        //     //echo 'Building and publishing multi-arch image to DockerHub..'
        //     //sh 'docker buildx build --push --platform linux/amd64,linux/arm64 -t jjulianbayon/labo:latest .'
        //    }
        //}
        //stage('Cleanup') {
        //    steps {
        //        echo 'Removing unused docker containers and images..'
        //        sh 'docker ps -aq | xargs --no-run-if-empty docker rm -f'
        //        // keep intermediate images as cache, only delete the final image
        //        sh 'docker images -q | xargs --no-run-if-empty docker rmi'
        //    }
        //}
          // Need to clean up
        stage("Destroy buildx builder") {
          steps {
            sh """
              docker buildx use default
              docker buildx rm $BUILDER_NAME

              ## Sanity check step
              docker buildx ls
            """
          }
        }
    }   
}

