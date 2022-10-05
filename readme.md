# Cloud Function Version History

---

## Hi!

This is Google Cloud Function API for object version history.

--

## Deploy

https://cloud.google.com/functions/docs/deploy

gcloud functions deploy YOUR_FUNCTION_NAME \
[--gen2] \
--region=YOUR_REGION \
--runtime=YOUR_RUNTIME \
--source=YOUR_SOURCE_LOCATION \
--entry-point=YOUR_CODE_ENTRYPOINT \
--min-instances=0 \
--max-instances=1 \
--memory=128
TRIGGER_FLAGS

gcloud functions deploy test_cf_221003 --region=asia-northeast3 --runtime=python37 --source=cloudfunction_version_history --entry-point=check_version_list --trigger-http

gcloud functions deploy test_cf_221004 --region=asia-northeast3 --runtime=python37 --source=cloudfunction_version_history --entry-point=check_version_list --trigger-http --min-instances=0 --max-instances=1 --memory=128
