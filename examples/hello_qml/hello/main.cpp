#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;

    // custom defines which cascade down from QMake (see ./package/package.pri)
    qDebug() << "PRODUCT_TITLE: "       << PRODUCT_TITLE;
    qDebug() << "PRODUCT_DESCRIPTION: " << PRODUCT_DESCRIPTION;
    qDebug() << "COMPANY_TRADE_NAME: "  << COMPANY_TRADE_NAME;
    qDebug() << "COMPANY_LEGAL_NAME: "  << COMPANY_LEGAL_NAME;
    qDebug() << "COPYRIGHT_YEAR: "      << COPYRIGHT_YEAR;
    qDebug() << "APP_VERSION: "         << APP_VERSION;

    // style the window
    QObject * rootObj = engine.rootObjects().first();
    rootObj->setProperty( "title", PRODUCT_TITLE );

    // set text on qml objects
    rootObj->findChild<QObject*>("product_title")->setProperty( "text", PRODUCT_TITLE );
    rootObj->findChild<QObject*>("app_version")->setProperty( "text", APP_VERSION );

    return app.exec();
}
