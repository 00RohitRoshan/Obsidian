redisS := getCredentials()
	redisCa, err := os.Create("ca.crt")
	if err != nil {
		fmt.Println("Error while creating ca cert file is", err.Error())
	}
	ssl_cert_file, err := os.Create("client.crt")
	if err != nil {
		fmt.Println("Error while creating ssl client certificate file is", err.Error())
	}

	ssl_key_file, err := os.Create("client.key")
	if err != nil {
		fmt.Println("Error while creating ssl client key file is", err.Error())
	}
	_, err = redisCa.WriteString(redisS.CA)
	if err != nil {
		fmt.Println("Error writing to ssl root ssl ca certificate file is", err.Error())
	}
	_, err = ssl_cert_file.WriteString(redisS.Tls)
	if err != nil {
		fmt.Println("Error writing to ssl client certificate file is", err.Error())
	}

	_, err = ssl_key_file.WriteString(redisS.Key)
	if err != nil {
		fmt.Println("Error writing to ssl key file is", err.Error())
	}
	caCert, err := os.ReadFile("ca.crt")
	if err != nil {
		log.Fatalf("Failed to read CA certificate: %v", err)
	}

	// Create a certificate pool and add the CA cert to it
	certPool := x509.NewCertPool()
	if !certPool.AppendCertsFromPEM(caCert) {
		// return nil, fmt.Errorf("failed to append CA cert")
		fmt.Println("failed to append CA cert")
	}
	clientCert, err := tls.LoadX509KeyPair("client.crt", "client.key")
	if err != nil {
		log.Fatalf("Failed to load client certificate and key: %v", err)
	}
	// Configure TLS settings
	tlsConfig := &tls.Config{
		RootCAs:            certPool,
		Certificates:       []tls.Certificate{clientCert},
		InsecureSkipVerify: true, // Ensures host verification
	}