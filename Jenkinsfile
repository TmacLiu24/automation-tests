pipeline {
    agent any
    
    stages {
        stage('环境准备') {
            steps {
                // 安装依赖
                sh 'pip install -r requirements.txt'
                // 安装Playwright浏览器
                sh 'playwright install chromium'
            }
        }
        
        stage('执行测试') {
            steps {
                // 运行异步测试脚本
                sh 'python tests/test_schedule_async.py'
            }
        }
    }
    
    post {
        always {
            // 保存测试结果
            archiveArtifacts artifacts: 'error_screenshot.png', allowEmptyArchive: true
        }
        success {
            echo '测试执行成功！'
        }
        failure {
            echo '测试执行失败！'
        }
    }
}
