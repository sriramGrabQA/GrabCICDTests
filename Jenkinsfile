pipeline {
  agent any
  stages {
    stage('SDP Tests') {
      parallel {
        stage('SDP Tests') {
          steps {
            sh 'echo SDP Tests running'
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