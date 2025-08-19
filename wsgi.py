from recipes import create_app
aoo = create_app()

if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)