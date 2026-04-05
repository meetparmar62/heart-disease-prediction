import sharp from 'sharp';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function convertToFavicon() {
    try {
        const inputFile = path.join(__dirname, 'public', 'logo.png');
        const outputFile = path.join(__dirname, 'public', 'favicon.ico');
        
        // Check if input file exists
        if (!fs.existsSync(inputFile)) {
            console.error('Input file not found:', inputFile);
            return;
        }

        // Convert PNG to ICO (32x32)
        await sharp(inputFile)
            .resize(32, 32)
            .toFormat('png')
            .toFile(outputFile.replace('.ico', '.png'));

        // Rename to .ico
        fs.renameSync(outputFile.replace('.ico', '.png'), outputFile);
        
        console.log('✓ Favicon created successfully:', outputFile);
        
        // Also create multiple sizes for better compatibility
        const sizes = [16, 32, 48, 64];
        
        for (const size of sizes) {
            await sharp(inputFile)
                .resize(size, size)
                .toFile(`public/favicon-${size}x${size}.png`);
            console.log(`✓ Created favicon-${size}x${size}.png`);
        }
        
    } catch (error) {
        console.error('Error creating favicon:', error);
    }
}

convertToFavicon();
