pipeline {
    agent {label 'node1'}

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            	}
	    }
	stage('print env'){
	    steps {
	      sh 'env'
	      sh 'pwd'
	      sh 'ls -ltr'
	    }

	  }
	stage('print username'){
	   steps{
	   	sh 'username'
	   }

	}
       }
}

