const puppeteer = require('puppeteer')

async function visit(obj){
	let browser;

	let url = obj['url'];
	let token = obj['token'];

	if(!/^https?:\/\//.test(url)){
		return;
	}

	try{
		browser = await puppeteer.launch({
            headless: true,
            executablePath: '/usr/bin/chromium-browser',
            args: [
            '--no-sandbox',
            '--headless',
            '--disable-gpu',
            '--disable-dev-shm-usage'
            ]
        });

		let page = await browser.newPage();
		await page.setCookie({
			name: 'token',
			value: token,
			domain: 'localhost',
			httpOnly: false,
			secure: true,
			sameSite: 'None',
			path: '/'
		});
		await page.goto(url,{ waitUntil: 'domcontentloaded', timeout: 3000 });
		await new Promise(r=>setTimeout(r,20000));
	}catch(e){ console.log(e) }
	try{await browser.close();}catch(e){}
	process.exit(0)
}

visit(JSON.parse(process.argv[2]))
