#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // custom defines which cascade down from QMake (see ./package/package.pri)
    qDebug() << "PRODUCT_TITLE: "       << PRODUCT_TITLE;
    qDebug() << "PRODUCT_DESCRIPTION: " << PRODUCT_DESCRIPTION;
    qDebug() << "COMPANY_NAME: "        << COMPANY_NAME;
    qDebug() << "COMPANY_LEGAL_NAME: "  << COMPANY_LEGAL_NAME;
    qDebug() << "COPYRIGHT_YEAR: "      << COPYRIGHT_YEAR;
    qDebug() << "APP_VERSION: "         << APP_VERSION;

    // style the window
    this->setWindowTitle( PRODUCT_TITLE );
    this->setWindowIcon( QIcon( ICON_RESOURCE_PATH ) );

    // set text on form labels
    ui->product_title->setText( PRODUCT_TITLE );
    ui->app_version->setText( APP_VERSION );
}

MainWindow::~MainWindow()
{
    delete ui;
}
