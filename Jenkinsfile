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
            sh '''echo VF Tests running
/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 -m robot CICD_Sanity_SIT.robot'''
          }
        }

      }
    }

  }
}