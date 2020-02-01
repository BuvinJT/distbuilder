#include <QGuiApplication>
#include <QQuickView>
#include <QDebug>

int main(int argc, char **argv)
{
    QGuiApplication app(argc, argv);

    QQuickView view;

    view.resize(500, 500);
    view.setResizeMode(QQuickView::SizeRootObjectToView);
    view.setSource(QUrl("qrc:/main.qml"));

    // custom defines which cascade down from QMake (see ./package/package.pri)
    qDebug() << "PRODUCT_TITLE: "       << PRODUCT_TITLE;
    qDebug() << "PRODUCT_DESCRIPTION: " << PRODUCT_DESCRIPTION;
    qDebug() << "COMPANY_TRADE_NAME: "  << COMPANY_TRADE_NAME;
    qDebug() << "COMPANY_LEGAL_NAME: "  << COMPANY_LEGAL_NAME;
    qDebug() << "COPYRIGHT_YEAR: "      << COPYRIGHT_YEAR;
    qDebug() << "APP_VERSION: "         << APP_VERSION;

    // style the window
    view.setTitle( PRODUCT_TITLE );

    // set text on qml objects
    QObject * rootObj = (QObject *)view.rootObject();
    rootObj->findChild<QObject*>("product_title")->setProperty( "text", PRODUCT_TITLE );
    rootObj->findChild<QObject*>("app_version")->setProperty( "text", APP_VERSION );

    view.show();

    return app.exec();
}
