properties([pipelineTriggers([pollSCM('* * * * *')])])


node {
    stage("clone"){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/yanivno/DevOps1411.git']]])
    }
    stage("show files"){
        sh "ls -al"
    }
}
