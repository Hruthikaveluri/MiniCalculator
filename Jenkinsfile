pipeline {
    agent { dockerfile true }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests With Coverage') {
            steps {
                sh 'coverage run -m pytest'
                sh 'coverage xml -o reports/coverage.xml'
                sh 'coverage html -d reports/htmlcov'
            }
        }

        stage('Publish Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/**/*', fingerprint: true

                publishHTML(target: [
                    allowMissing: false,
                    keepAll: true,
                    reportDir: 'reports/htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }
}
