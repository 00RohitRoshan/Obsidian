type SMpayload struct {
	Hostname string `json:"hostname"`
	IP       string `json:"ip"`
	Port     string `json:"port"`
	Username string `json:"username"`
	Password string `json:"password"`
	CA       string `json:"ca"`
	Tls      string `json:"tls"`
	Key      string `json:"key"`
}
func getCredentials() SMpayload {
	// const redisusername= "rd_api_gateway_redev_stag_rw"
	// const redisHost="35.200.161.89"
	// const redisPort="6379"
	// const redispassword="r35eARch_@NdDeV"
	const secretName = "projects/720089661819/secrets/redis-stag-rd_api_gateway_redev_stag_rw-user/versions/1"
	var SMpayload SMpayload
	ctx := context.Background()
	clientfordb, err1 := secretmanager.NewClient(ctx)
	if err1 != nil {
		fmt.Println("Error in client connection", err1)
		// return err1
	}
	defer clientfordb.Close()
	// secretName := os.Getenv("SecretName")

	fmt.Println("Secret manager url:", secretName)
	// Retrieve the secret
	secretVersion, err := clientfordb.AccessSecretVersion(ctx, &secretmanagerpb.AccessSecretVersionRequest{
		Name: secretName,
	})
	if err != nil {
		fmt.Println("SMerror : ", err)
	} else {
		err = json.Unmarshal(secretVersion.Payload.Data, &SMpayload)
		if err != nil {
			fmt.Println("error in unmarshaling secret data for db", err)
			fmt.Println("Unmarshal error", err)
		}
		fmt.Println("SMdata : ", SMpayload)
	}
	return SMpayload
}