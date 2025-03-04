	// err := godotenv.Load("config.env") // Load .env file
	// if err != nil {
	// 	log.Fatal("Error loading .env file :", err)
	// }
	// var red_err error
	// var c redis.Conn
	redisS := getCredentials()

	// Create a certificate pool and add the CA cert to it
	certPool := x509.NewCertPool()
	if !certPool.AppendCertsFromPEM([]byte(redisS.CA)) {
		// return nil, fmt.Errorf("failed to append CA cert")
	}

	// Create a custom TLS configuration with the CA cert
	tlsConfig := &tls.Config{
		RootCAs:            certPool,
		InsecureSkipVerify: true, // Make sure server certificates are verified
	}
	redispool = &redis.Pool{
		MaxIdle:     3000,
		MaxActive:   4500,
		IdleTimeout: 10 * time.Second,
		Dial: func() (redis.Conn, error) {
			c, err := redis.Dial("tcp", redisS.IP+":"+redisS.Port,
				redis.DialUsername(redisS.Username),
				redis.DialPassword(redisS.Password),
				redis.DialUseTLS(true),
				redis.DialTLSSkipVerify(true),
				redis.DialTLSConfig(tlsConfig))
			if err != nil {
				return nil, err
			}
			return c, nil
		},
	}
	fmt.Println("redis pool connection completed")