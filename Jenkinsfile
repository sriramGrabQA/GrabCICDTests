pipeline {
  agent any
  stages {
    stage('Sanity Tests') {
      parallel {
        stage('SDP Tests') {
          steps {
            sh '''echo SDP Tests running
pwd'''
          }
        }

        stage('VF Tests') {
          steps {
            sh 'echo VF Tests running'
          }
        }

      }
    }

  }
}